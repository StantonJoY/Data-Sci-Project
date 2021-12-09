Module(
    body=[
        Import(
            names=[alias(name='random', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='textwrap', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='datetime', asname=None),
                alias(name='timedelta', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[
                alias(name='BaseCase', asname=None),
                alias(name='tagged', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='topological_sort', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.web.controllers.main',
            names=[alias(name='HomeStaticTemplateHelpers', asname=None)],
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
        FunctionDef(
            name='sample',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='population', annotation=None, type_comment=None)],
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
                            value=Name(id='random', ctx=Load()),
                            attr='sample',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='population', ctx=Load()),
                            Call(
                                func=Attribute(
                                    value=Name(id='random', ctx=Load()),
                                    attr='randint',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=0, kind=None),
                                    Call(
                                        func=Name(id='min', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='population', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value=5, kind=None),
                                        ],
                                        keywords=[],
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
        ClassDef(
            name='TestModulesLoading',
            bases=[Name(id='BaseCase', ctx=Load())],
            keywords=[],
            body=[
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mods',
                                    ctx=Store(),
                                ),
                            ],
                            value=ListComp(
                                elt=Call(
                                    func=Name(id='str', ctx=Load()),
                                    args=[Name(id='i', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='i', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='range', ctx=Load()),
                                            args=[Constant(value=1000, kind=None)],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_topological_sort',
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
                                    value=Name(id='random', ctx=Load()),
                                    attr='shuffle',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='mods',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='modules', ctx=Store())],
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Name(id='k', ctx=Load()),
                                        Call(
                                            func=Name(id='sample', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='mods',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Slice(
                                                        lower=None,
                                                        upper=Name(id='i', ctx=Load()),
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='i', ctx=Store()),
                                                Name(id='k', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Name(id='enumerate', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mods',
                                                    ctx=Load(),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='random', ctx=Load()),
                                    attr='shuffle',
                                    ctx=Load(),
                                ),
                                args=[Name(id='modules', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ms', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[Name(id='modules', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='seen', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sorted_modules', ctx=Store())],
                            value=Call(
                                func=Name(id='topological_sort', ctx=Load()),
                                args=[Name(id='ms', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='module', ctx=Store()),
                            iter=Name(id='sorted_modules', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='deps', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='ms', ctx=Load()),
                                        slice=Name(id='module', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertGreaterEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='seen', ctx=Load()),
                                            Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[Name(id='deps', ctx=Load())],
                                                keywords=[],
                                            ),
                                            BinOp(
                                                left=Constant(value='Module %s (index %d), missing dependencies %s from loaded modules %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='module', ctx=Load()),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='sorted_modules', ctx=Load()),
                                                                attr='index',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='module', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        Name(id='deps', ctx=Load()),
                                                        Name(id='seen', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='seen', ctx=Load()),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='module', ctx=Load())],
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
            decorator_list=[],
        ),
        ClassDef(
            name='TestStaticInheritanceCommon',
            bases=[Name(id='BaseCase', ctx=Load())],
            keywords=[],
            body=[
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
                                        args=[
                                            Name(id='TestStaticInheritanceCommon', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='asset_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_1', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='module_2_file_1', kind=None),
                                            Constant(value='module_2', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='module_1_file_1', kind=None),
                                    Constant(value='module_2_file_1', kind=None),
                                ],
                                values=[
                                    Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_1_1" random-attr="gloria">\n                        <div>At first I was afraid</div>\n                        <div>Kept thinking I could never live without you by my side</div>\n                    </form>\n                    <t t-name="template_1_2">\n                        <div>And I grew strong</div>\n                    </t>\n                </templates>\n                ', kind=None),
                                    Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_2_1" t-inherit="module_1.template_1_1" t-inherit-mode="primary">\n                        <xpath expr="//div[1]" position="after">\n                            <div>I was petrified</div>\n                        </xpath>\n                        <xpath expr="//div[2]" position="after">\n                            <div>But then I spent so many nights thinking how you did me wrong</div>\n                        </xpath>\n                    </form>\n                    <div t-name="template_2_2">\n                        <div>And I learned how to get along</div>\n                    </div>\n                    <form t-inherit="module_1.template_1_2" t-inherit-mode="extension">\n                        <xpath expr="//div[1]" position="after">\n                            <div>And I learned how to get along</div>\n                        </xpath>\n                    </form>\n                </templates>\n                ', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_set_patchers',
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
                                    attr='_toggle_patchers',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='start', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_reg_replace_ws',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='\\s|\\t', kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='tearDown',
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
                                        args=[
                                            Name(id='TestStaticInheritanceCommon', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='tearDown',
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
                                    attr='_toggle_patchers',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='stop', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertXMLEqual',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='output', annotation=None, type_comment=None),
                            arg(arg='expected', annotation=None, type_comment=None),
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[Name(id='output', ctx=Load())],
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
                                args=[Name(id='expected', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='output', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='textwrap', ctx=Load()),
                                            attr='dedent',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='output', ctx=Load()),
                                                    attr='decode',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='UTF-8', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='strip',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='output', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_reg_replace_ws',
                                        ctx=Load(),
                                    ),
                                    Constant(value='', kind=None),
                                    Name(id='output', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='textwrap', ctx=Load()),
                                            attr='dedent',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='expected', ctx=Load()),
                                                    attr='decode',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='UTF-8', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='strip',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_reg_replace_ws',
                                        ctx=Load(),
                                    ),
                                    Constant(value='', kind=None),
                                    Name(id='expected', ctx=Load()),
                                ],
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
                                    Name(id='output', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='_get_module_names',
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
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=',', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='asset_path', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='asset_path', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='asset_paths',
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_set_patchers',
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
                        FunctionDef(
                            name='_patched_for_get_asset_paths',
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
                                Return(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='asset_paths',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='_patch_for_read_addon_file',
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
                                Return(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='template_files',
                                            ctx=Load(),
                                        ),
                                        slice=Subscript(
                                            value=Name(id='args', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='patchers',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                            Constant(value='_get_asset_paths', kind=None),
                                            Name(id='_patched_for_get_asset_paths', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                            Constant(value='_read_addon_file', kind=None),
                                            Name(id='_patch_for_read_addon_file', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_toggle_patchers',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='mode', annotation=None, type_comment=None),
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Compare(
                                        left=Name(id='mode', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='start', kind=None),
                                                    Constant(value='stop', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='p', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='patchers',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Call(
                                            func=Name(id='getattr', ctx=Load()),
                                            args=[
                                                Name(id='p', ctx=Load()),
                                                Name(id='mode', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        args=[],
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
            decorator_list=[],
        ),
        ClassDef(
            name='TestStaticInheritance',
            bases=[Name(id='TestStaticInheritanceCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_static_inheritance_01',
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
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value=b'\n            <templates>\n                <form t-name="template_1_1" random-attr="gloria">\n                    <div>At first I was afraid</div>\n                    <div>Kept thinking I could never live without you by my side</div>\n                </form>\n                <t t-name="template_1_2">\n                    <div>And I grew strong</div>\n                    <div>And I learned how to get along</div>\n                </t>\n                <form t-name="template_2_1" random-attr="gloria">\n                    <div>At first I was afraid</div>\n                    <div>I was petrified</div>\n                    <div>But then I spent so many nights thinking how you did me wrong</div>\n                    <div>Kept thinking I could never live without you by my side</div>\n                </form>\n                <div t-name="template_2_2">\n                    <div>And I learned how to get along</div>\n                </div>\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='contents', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_static_inheritance_02',
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
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[Constant(value='module_1_file_1', kind=None)],
                                values=[Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_1_1" random-attr="gloria">\n                        <div>At first I was afraid</div>\n                        <div>Kept thinking I could never live without you by my side</div>\n                    </form>\n                    <form t-name="template_1_2" t-inherit="template_1_1" added="true">\n                        <xpath expr="//div[1]" position="after">\n                            <div>I was petrified</div>\n                        </xpath>\n                    </form>\n                </templates>\n            ', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='asset_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_1', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value=b'\n            <templates>\n                <form t-name="template_1_1" random-attr="gloria">\n                    <div>At first I was afraid</div>\n                    <div>Kept thinking I could never live without you by my side</div>\n                </form>\n                <form t-name="template_1_2" random-attr="gloria" added="true">\n                    <div>At first I was afraid</div>\n                    <div>I was petrified</div>\n                    <div>Kept thinking I could never live without you by my side</div>\n                </form>\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='contents', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_static_inheritance_03',
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
                                    attr='maxDiff',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[Constant(value='module_1_file_1', kind=None)],
                                values=[Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_1_1">\n                        <div>At first I was afraid</div>\n                        <div>Kept thinking I could never live without you by my side</div>\n                    </form>\n                    <form t-name="template_1_2" t-inherit="template_1_1" added="true">\n                        <xpath expr="//div[1]" position="after">\n                            <div>I was petrified</div>\n                        </xpath>\n                    </form>\n                    <form t-name="template_1_3" t-inherit="template_1_2" added="false" other="here">\n                        <xpath expr="//div[2]" position="replace"/>\n                    </form>\n                </templates>\n            ', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='asset_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_1', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value=b'\n            <templates>\n                <form t-name="template_1_1">\n                    <div>At first I was afraid</div>\n                    <div>Kept thinking I could never live without you by my side</div>\n                </form>\n                <form t-name="template_1_2" added="true">\n                    <div>At first I was afraid</div>\n                    <div>I was petrified</div>\n                    <div>Kept thinking I could never live without you by my side</div>\n                </form>\n                <form t-name="template_1_3" added="false" other="here">\n                    <div>At first I was afraid</div>\n                    <div>Kept thinking I could never live without you by my side</div>\n                </form>\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='contents', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_static_inheritance_in_same_module',
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
                                    attr='asset_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_1', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_2', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='module_1_file_1', kind=None),
                                    Constant(value='module_1_file_2', kind=None),
                                ],
                                values=[
                                    Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_1_1">\n                        <div>At first I was afraid</div>\n                        <div>Kept thinking I could never live without you by my side</div>\n                    </form>\n                </templates>\n            ', kind=None),
                                    Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_1_2" t-inherit="template_1_1" t-inherit-mode="primary">\n                        <xpath expr="//div[1]" position="after">\n                            <div>I was petrified</div>\n                        </xpath>\n                    </form>\n                </templates>\n            ', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value=b'\n            <templates>\n                <form t-name="template_1_1">\n                    <div>At first I was afraid</div>\n                    <div>Kept thinking I could never live without you by my side</div>\n                </form>\n                <form t-name="template_1_2">\n                    <div>At first I was afraid</div>\n                    <div>I was petrified</div>\n                    <div>Kept thinking I could never live without you by my side</div>\n                </form>\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='contents', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_static_inheritance_in_same_file',
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
                                    attr='asset_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_1', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[Constant(value='module_1_file_1', kind=None)],
                                values=[Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_1_1">\n                        <div>At first I was afraid</div>\n                        <div>Kept thinking I could never live without you by my side</div>\n                    </form>\n                    <form t-name="template_1_2" t-inherit="template_1_1" t-inherit-mode="primary">\n                        <xpath expr="//div[1]" position="after">\n                            <div>I was petrified</div>\n                        </xpath>\n                    </form>\n                </templates>\n            ', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value=b'\n            <templates>\n                <form t-name="template_1_1">\n                    <div>At first I was afraid</div>\n                    <div>Kept thinking I could never live without you by my side</div>\n                </form>\n                <form t-name="template_1_2">\n                    <div>At first I was afraid</div>\n                    <div>I was petrified</div>\n                    <div>Kept thinking I could never live without you by my side</div>\n                </form>\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='contents', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_static_inherit_extended_template',
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
                                    attr='asset_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_1', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[Constant(value='module_1_file_1', kind=None)],
                                values=[Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_1_1">\n                        <div>At first I was afraid</div>\n                        <div>Kept thinking I could never live without you by my side</div>\n                    </form>\n                    <form t-name="template_1_2" t-inherit="template_1_1" t-inherit-mode="extension">\n                        <xpath expr="//div[1]" position="after">\n                            <div>I was petrified</div>\n                        </xpath>\n                    </form>\n                    <form t-name="template_1_3" t-inherit="template_1_1" t-inherit-mode="primary">\n                        <xpath expr="//div[3]" position="after">\n                            <div>But then I spent so many nights thinking how you did me wrong</div>\n                        </xpath>\n                    </form>\n                </templates>\n            ', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value=b'\n            <templates>\n                <form t-name="template_1_1">\n                    <div>At first I was afraid</div>\n                    <div>I was petrified</div>\n                    <div>Kept thinking I could never live without you by my side</div>\n                </form>\n                <form t-name="template_1_3">\n                    <div>At first I was afraid</div>\n                    <div>I was petrified</div>\n                    <div>Kept thinking I could never live without you by my side</div>\n                    <div>But then I spent so many nights thinking how you did me wrong</div>\n                </form>\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='contents', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_sibling_extension',
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
                                    attr='asset_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_1', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='module_2_file_1', kind=None),
                                            Constant(value='module_2', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='module_3_file_1', kind=None),
                                            Constant(value='module_3', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='module_1_file_1', kind=None),
                                    Constant(value='module_2_file_1', kind=None),
                                    Constant(value='module_3_file_1', kind=None),
                                ],
                                values=[
                                    Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_1_1">\n                        <div>I am a man of constant sorrow</div>\n                        <div>I\'ve seen trouble all my days</div>\n                    </form>\n                </templates>\n            ', kind=None),
                                    Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_2_1" t-inherit="module_1.template_1_1" t-inherit-mode="extension">\n                        <xpath expr="//div[1]" position="after">\n                            <div>In constant sorrow all through his days</div>\n                        </xpath>\n                    </form>\n                </templates>\n            ', kind=None),
                                    Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_3_1" t-inherit="module_1.template_1_1" t-inherit-mode="extension">\n                        <xpath expr="//div[2]" position="after">\n                            <div>Oh Brother !</div>\n                        </xpath>\n                    </form>\n                </templates>\n            ', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value=b'\n            <templates>\n                <form t-name="template_1_1">\n                    <div>I am a man of constant sorrow</div>\n                    <div>In constant sorrow all through his days</div>\n                    <div>Oh Brother !</div>\n                    <div>I\'ve seen trouble all my days</div>\n                </form>\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='contents', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_static_misordered_modules',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='asset_paths',
                                        ctx=Load(),
                                    ),
                                    attr='reverse',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValueError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='ve', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                            attr='get_qweb_templates',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='addons',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_get_module_names',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='debug',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
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
                                        func=Name(id='str', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='ve', ctx=Load()),
                                                attr='exception',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='Module module_1 not loaded or inexistent, or templates of addon being loaded (module_2) are misordered', kind=None),
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
                    name='test_static_misordered_templates',
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
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='template_files',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='module_2_file_1', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=b'\n            <templates id="template" xml:space="preserve">\n                <form t-name="template_2_1" t-inherit="module_2.template_2_2" t-inherit-mode="primary">\n                    <xpath expr="//div[1]" position="after">\n                        <div>I was petrified</div>\n                    </xpath>\n                </form>\n                <div t-name="template_2_2">\n                    <div>And I learned how to get along</div>\n                </div>\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValueError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='ve', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                            attr='get_qweb_templates',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='addons',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_get_module_names',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='debug',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
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
                                        func=Name(id='str', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='ve', ctx=Load()),
                                                attr='exception',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='No template found to inherit from. Module module_2 and template name template_2_2', kind=None),
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
                    name='test_replace_in_debug_mode',
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
                            value=Constant(value="\n        Replacing a template's meta definition in place doesn't keep the original attrs of the template\n        ", kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='asset_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_1', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[Constant(value='module_1_file_1', kind=None)],
                                values=[Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_1_1" random-attr="gloria">\n                        <div>At first I was afraid</div>\n                    </form>\n                    <t t-name="template_1_2" t-inherit="template_1_1" t-inherit-mode="extension">\n                        <xpath expr="." position="replace">\n                            <div overriden-attr="overriden">And I grew strong</div>\n                        </xpath>\n                    </t>\n                </templates>\n                ', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value=b'\n            <templates>\n                <div overriden-attr="overriden" t-name="template_1_1">\n                    And I grew strong\n                </div>\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='contents', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_replace_in_debug_mode2',
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
                                    attr='asset_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_1', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[Constant(value='module_1_file_1', kind=None)],
                                values=[Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_1_1" random-attr="gloria">\n                        <div>At first I was afraid</div>\n                    </form>\n                    <t t-name="template_1_2" t-inherit="template_1_1" t-inherit-mode="extension">\n                        <xpath expr="." position="replace">\n                            <div>\n                                And I grew strong\n                                <p>And I learned how to get along</p>\n                                And so you\'re back\n                            </div>\n                        </xpath>\n                    </t>\n                </templates>\n                ', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value=b'\n            <templates>\n                <div t-name="template_1_1">\n                    And I grew strong\n                    <p>And I learned how to get along</p>\n                    And so you\'re back\n                </div>\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='contents', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_replace_in_debug_mode3',
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
                            value=Constant(value="Text outside of a div which will replace a whole template\n        becomes outside of the template\n        This doesn't mean anything in terms of the business of template inheritance\n        But it is in the XPATH specs", kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='asset_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_1', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[Constant(value='module_1_file_1', kind=None)],
                                values=[Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_1_1" random-attr="gloria">\n                        <div>At first I was afraid</div>\n                    </form>\n                    <t t-name="template_1_2" t-inherit="template_1_1" t-inherit-mode="extension">\n                        <xpath expr="." position="replace">\n                            <div>\n                                And I grew strong\n                                <p>And I learned how to get along</p>\n                            </div>\n                            And so you\'re back\n                        </xpath>\n                    </t>\n                </templates>\n                ', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value=b'\n            <templates>\n                <div t-name="template_1_1">\n                    And I grew strong\n                    <p>And I learned how to get along</p>\n                </div>\n                And so you\'re back\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='contents', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_replace_root_node_tag',
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
                            value=Constant(value='\n        Root node IS targeted by //NODE_TAG in xpath\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='asset_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_1', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[Constant(value='module_1_file_1', kind=None)],
                                values=[Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_1_1" random-attr="gloria">\n                        <div>At first I was afraid</div>\n                        <form>Inner Form</form>\n                    </form>\n                    <t t-name="template_1_2" t-inherit="template_1_1" t-inherit-mode="extension">\n                        <xpath expr="//form" position="replace">\n                            <div>\n                                Form replacer\n                            </div>\n                        </xpath>\n                    </t>\n                </templates>\n                ', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value=b'\n            <templates>\n                <div t-name="template_1_1">\n                    Form replacer\n                </div>\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='contents', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_replace_root_node_tag_in_primary',
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
                            value=Constant(value='\n        Root node IS targeted by //NODE_TAG in xpath\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='maxDiff',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='asset_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_1', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[Constant(value='module_1_file_1', kind=None)],
                                values=[Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_1_1" random-attr="gloria">\n                        <div>At first I was afraid</div>\n                        <form>Inner Form</form>\n                    </form>\n                    <form t-name="template_1_2" t-inherit="template_1_1" t-inherit-mode="primary">\n                        <xpath expr="//form" position="replace">\n                            <div>Form replacer</div>\n                        </xpath>\n                    </form>\n                </templates>\n                ', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value=b'\n            <templates>\n                <form t-name="template_1_1" random-attr="gloria">\n                    <div>At first I was afraid</div>\n                    <form>Inner Form</form>\n                </form>\n                <div t-name="template_1_2">\n                    Form replacer\n                </div>\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='contents', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_inherit_primary_replace_debug',
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
                            value=Constant(value='\n        The inheriting template has got both its own defining attrs\n        and new ones if one is to replace its defining root node\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='asset_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_1', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[Constant(value='module_1_file_1', kind=None)],
                                values=[Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_1_1" random-attr="gloria">\n                        <div>At first I was afraid</div>\n                    </form>\n                    <t t-name="template_1_2" t-inherit="template_1_1" t-inherit-mode="primary">\n                        <xpath expr="." position="replace">\n                            <div overriden-attr="overriden">\n                                And I grew strong\n                                <p>And I learned how to get along</p>\n                            </div>\n                        </xpath>\n                    </t>\n                </templates>\n                ', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value=b'\n            <templates>\n                <form t-name="template_1_1" random-attr="gloria">\n                    <div>At first I was afraid</div>\n                 </form>\n                 <div overriden-attr="overriden" t-name="template_1_2">\n                    And I grew strong\n                    <p>And I learned how to get along</p>\n                 </div>\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='contents', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_replace_in_nodebug_mode1',
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
                            value=Constant(value='Comments already in the arch are ignored', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='asset_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_1', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[Constant(value='module_1_file_1', kind=None)],
                                values=[Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_1_1" random-attr="gloria">\n                        <div>At first I was afraid</div>\n                    </form>\n                    <t t-name="template_1_2" t-inherit="template_1_1" t-inherit-mode="extension">\n                        <xpath expr="." position="replace">\n                            <div>\n                                <!-- Random Comment -->\n                                And I grew strong\n                                <p>And I learned how to get along</p>\n                                And so you\'re back\n                            </div>\n                        </xpath>\n                    </t>\n                </templates>\n                ', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value=b'\n            <templates>\n                <div t-name="template_1_1">\n                    And I grew strong\n                    <p>And I learned how to get along</p>\n                    And so you\'re back\n                </div>\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='contents', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_inherit_from_dotted_tname_1',
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
                                    attr='asset_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_1', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[Constant(value='module_1_file_1', kind=None)],
                                values=[Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="module_1.template_1_1.dot" random-attr="gloria">\n                        <div>At first I was afraid</div>\n                    </form>\n                    <t t-name="template_1_2" t-inherit="template_1_1.dot" t-inherit-mode="primary">\n                        <xpath expr="." position="replace">\n                            <div overriden-attr="overriden">\n                                And I grew strong\n                                <p>And I learned how to get along</p>\n                            </div>\n                        </xpath>\n                    </t>\n                </templates>\n                ', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value=b'\n            <templates>\n                <form t-name="module_1.template_1_1.dot" random-attr="gloria">\n                    <div>At first I was afraid</div>\n                 </form>\n                 <div overriden-attr="overriden" t-name="template_1_2">\n                    And I grew strong\n                    <p>And I learned how to get along</p>\n                 </div>\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='contents', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_inherit_from_dotted_tname_2',
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
                                    attr='asset_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_1', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[Constant(value='module_1_file_1', kind=None)],
                                values=[Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_1_1.dot" random-attr="gloria">\n                        <div>At first I was afraid</div>\n                    </form>\n                    <t t-name="template_1_2" t-inherit="template_1_1.dot" t-inherit-mode="primary">\n                        <xpath expr="." position="replace">\n                            <div overriden-attr="overriden">\n                                And I grew strong\n                                <p>And I learned how to get along</p>\n                            </div>\n                        </xpath>\n                    </t>\n                </templates>\n                ', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value=b'\n            <templates>\n                <form t-name="template_1_1.dot" random-attr="gloria">\n                    <div>At first I was afraid</div>\n                 </form>\n                 <div overriden-attr="overriden" t-name="template_1_2">\n                    And I grew strong\n                    <p>And I learned how to get along</p>\n                 </div>\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='contents', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_inherit_from_dotted_tname_2bis',
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
                                    attr='asset_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_1', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[Constant(value='module_1_file_1', kind=None)],
                                values=[Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="template_1_1.dot" random-attr="gloria">\n                        <div>At first I was afraid</div>\n                    </form>\n                    <t t-name="template_1_2" t-inherit="module_1.template_1_1.dot" t-inherit-mode="primary">\n                        <xpath expr="." position="replace">\n                            <div overriden-attr="overriden">\n                                And I grew strong\n                                <p>And I learned how to get along</p>\n                            </div>\n                        </xpath>\n                    </t>\n                </templates>\n                ', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value=b'\n            <templates>\n                <form t-name="template_1_1.dot" random-attr="gloria">\n                    <div>At first I was afraid</div>\n                 </form>\n                 <div overriden-attr="overriden" t-name="template_1_2">\n                    And I grew strong\n                    <p>And I learned how to get along</p>\n                 </div>\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='contents', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_inherit_from_dotted_tname_2ter',
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
                                    attr='asset_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_1', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[Constant(value='module_1_file_1', kind=None)],
                                values=[Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="module_1" random-attr="gloria">\n                        <div>At first I was afraid</div>\n                    </form>\n                    <t t-name="template_1_2" t-inherit="module_1" t-inherit-mode="primary">\n                        <xpath expr="." position="replace">\n                            <div overriden-attr="overriden">\n                                And I grew strong\n                                <p>And I learned how to get along</p>\n                            </div>\n                        </xpath>\n                    </t>\n                </templates>\n                ', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value=b'\n            <templates>\n                <form t-name="module_1" random-attr="gloria">\n                    <div>At first I was afraid</div>\n                 </form>\n                 <div overriden-attr="overriden" t-name="template_1_2">\n                    And I grew strong\n                    <p>And I learned how to get along</p>\n                 </div>\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='contents', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_inherit_from_dotted_tname_3',
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
                                    attr='asset_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module_1_file_1', kind=None),
                                            Constant(value='module_1', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='module_2_file_1', kind=None),
                                            Constant(value='module_2', kind=None),
                                            Constant(value='bundle_1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='module_1_file_1', kind=None),
                                    Constant(value='module_2_file_1', kind=None),
                                ],
                                values=[
                                    Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <form t-name="module_1.template_1_1.dot" random-attr="gloria">\n                        <div>At first I was afraid</div>\n                    </form>\n                </templates>\n                ', kind=None),
                                    Constant(value=b'\n                <templates id="template" xml:space="preserve">\n                    <t t-name="template_2_1" t-inherit="module_1.template_1_1.dot" t-inherit-mode="primary">\n                        <xpath expr="." position="replace">\n                            <div overriden-attr="overriden">\n                                And I grew strong\n                                <p>And I learned how to get along</p>\n                            </div>\n                        </xpath>\n                    </t>\n                </templates>\n            ', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value=b'\n            <templates>\n                <form t-name="module_1.template_1_1.dot" random-attr="gloria">\n                    <div>At first I was afraid</div>\n                 </form>\n                 <div overriden-attr="overriden" t-name="template_2_1">\n                    And I grew strong\n                    <p>And I learned how to get along</p>\n                 </div>\n            </templates>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXMLEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='contents', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    func=Name(id='tagged', ctx=Load()),
                    args=[Constant(value='static_templates', kind=None)],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            name='TestStaticInheritancePerformance',
            bases=[Name(id='TestStaticInheritanceCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='_sick_script',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='nMod', annotation=None, type_comment=None),
                            arg(arg='nFilePerMod', annotation=None, type_comment=None),
                            arg(arg='nTemplatePerFile', annotation=None, type_comment=None),
                            arg(arg='stepInheritInModule', annotation=None, type_comment=None),
                            arg(arg='stepInheritPreviousModule', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=2, kind=None),
                            Constant(value=3, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Make a sick amount of templates to test perf\n        nMod modules\n        each module: has nFilesPerModule files, each of which contains nTemplatePerFile templates\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='asset_paths',
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
                                    attr='template_files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='number_templates', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='m', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[Name(id='nMod', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='f', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[Name(id='nFilePerMod', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='mname', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='mod_%s', kind=None),
                                                op=Mod(),
                                                right=Name(id='m', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='fname', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='mod_%s_file_%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='m', ctx=Load()),
                                                        Name(id='f', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='asset_paths',
                                                        ctx=Load(),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='fname', ctx=Load()),
                                                            Name(id='mname', ctx=Load()),
                                                            Constant(value='bundle_1', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='_file', ctx=Store())],
                                            value=Constant(value='<templates id="template" xml:space="preserve">', kind=None),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='t', ctx=Store()),
                                            iter=Call(
                                                func=Name(id='range', ctx=Load()),
                                                args=[Name(id='nTemplatePerFile', ctx=Load())],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='_template', ctx=Store())],
                                                    value=Constant(value='', kind=None),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BinOp(
                                                                left=Name(id='t', ctx=Load()),
                                                                op=Mod(),
                                                                right=Name(id='stepInheritInModule', ctx=Load()),
                                                            ),
                                                            BinOp(
                                                                left=Name(id='t', ctx=Load()),
                                                                op=Mod(),
                                                                right=Name(id='stepInheritPreviousModule', ctx=Load()),
                                                            ),
                                                            Compare(
                                                                left=Name(id='t', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value=0, kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='_template', ctx=Store()),
                                                            op=Add(),
                                                            value=Constant(value='\n                            <div t-name="template_%(t_number)s_mod_%(m_number)s">\n                                <div>Parent</div>\n                            </div>\n                        ', kind=None),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    UnaryOp(
                                                                        op=Not(),
                                                                        operand=BinOp(
                                                                            left=Name(id='t', ctx=Load()),
                                                                            op=Mod(),
                                                                            right=Name(id='stepInheritInModule', ctx=Load()),
                                                                        ),
                                                                    ),
                                                                    Compare(
                                                                        left=Name(id='t', ctx=Load()),
                                                                        ops=[GtE()],
                                                                        comparators=[Constant(value=1, kind=None)],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                AugAssign(
                                                                    target=Name(id='_template', ctx=Store()),
                                                                    op=Add(),
                                                                    value=Constant(value='\n                            <div t-name="template_%(t_number)s_mod_%(m_number)s"\n                                t-inherit="template_%(t_inherit)s_mod_%(m_number)s"\n                                t-inherit-mode="primary">\n                                <xpath expr="/div/div[1]" position="before">\n                                    <div>Sick XPath</div>\n                                </xpath>\n                            </div>\n                        ', kind=None),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            UnaryOp(
                                                                                op=Not(),
                                                                                operand=BinOp(
                                                                                    left=Name(id='t', ctx=Load()),
                                                                                    op=Mod(),
                                                                                    right=Name(id='stepInheritPreviousModule', ctx=Load()),
                                                                                ),
                                                                            ),
                                                                            Compare(
                                                                                left=Name(id='m', ctx=Load()),
                                                                                ops=[GtE()],
                                                                                comparators=[Constant(value=1, kind=None)],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        AugAssign(
                                                                            target=Name(id='_template', ctx=Store()),
                                                                            op=Add(),
                                                                            value=Constant(value='\n                            <div t-name="template_%(t_number)s_mod_%(m_number)s"\n                                t-inherit="mod_%(m_module_inherit)s.template_%(t_module_inherit)s_mod_%(m_module_inherit)s"\n                                t-inherit-mode="primary">\n                                <xpath expr="/div/div[1]" position="inside">\n                                    <div>Mental XPath</div>\n                                </xpath>\n                            </div>\n                        ', kind=None),
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                If(
                                                    test=Name(id='_template', ctx=Load()),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='number_templates', ctx=Store()),
                                                            op=Add(),
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='_template_number', ctx=Store())],
                                                    value=BinOp(
                                                        left=BinOp(
                                                            left=Constant(value=1000, kind=None),
                                                            op=Mult(),
                                                            right=Name(id='f', ctx=Load()),
                                                        ),
                                                        op=Add(),
                                                        right=Name(id='t', ctx=Load()),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                AugAssign(
                                                    target=Name(id='_file', ctx=Store()),
                                                    op=Add(),
                                                    value=BinOp(
                                                        left=Name(id='_template', ctx=Load()),
                                                        op=Mod(),
                                                        right=Dict(
                                                            keys=[
                                                                Constant(value='t_number', kind=None),
                                                                Constant(value='m_number', kind=None),
                                                                Constant(value='t_inherit', kind=None),
                                                                Constant(value='t_module_inherit', kind=None),
                                                                Constant(value='m_module_inherit', kind=None),
                                                            ],
                                                            values=[
                                                                Name(id='_template_number', ctx=Load()),
                                                                Name(id='m', ctx=Load()),
                                                                BinOp(
                                                                    left=Name(id='_template_number', ctx=Load()),
                                                                    op=Sub(),
                                                                    right=Constant(value=1, kind=None),
                                                                ),
                                                                Name(id='_template_number', ctx=Load()),
                                                                BinOp(
                                                                    left=Name(id='m', ctx=Load()),
                                                                    op=Sub(),
                                                                    right=Constant(value=1, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Name(id='_file', ctx=Store()),
                                            op=Add(),
                                            value=Constant(value='</templates>', kind=None),
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='template_files',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='fname', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_file', ctx=Load()),
                                                    attr='encode',
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
                            ],
                            orelse=[],
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
                                    Name(id='number_templates', ctx=Load()),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='nMod', ctx=Load()),
                                            op=Mult(),
                                            right=Name(id='nFilePerMod', ctx=Load()),
                                        ),
                                        op=Mult(),
                                        right=Name(id='nTemplatePerFile', ctx=Load()),
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
                    name='test_static_templates_treatment_linearity',
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
                                Tuple(
                                    elts=[
                                        Name(id='nMod', ctx=Store()),
                                        Name(id='nFilePerMod', ctx=Store()),
                                        Name(id='nTemplatePerFile', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Constant(value=50, kind=None),
                                    Constant(value=5, kind=None),
                                    Constant(value=10, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_sick_script',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='nMod', ctx=Load()),
                                    Name(id='nFilePerMod', ctx=Load()),
                                    Name(id='nTemplatePerFile', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='before', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='now',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='contents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='after', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='now',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='delta2500', ctx=Store())],
                            value=BinOp(
                                left=Name(id='after', ctx=Load()),
                                op=Sub(),
                                right=Name(id='before', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='runbot',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='Static Templates Inheritance: 2500 templates treated in %s seconds', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='delta2500', ctx=Load()),
                                                attr='total_seconds',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='whole_tree', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[Name(id='contents', ctx=Load())],
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
                                        args=[Name(id='whole_tree', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='nMod', ctx=Load()),
                                            op=Mult(),
                                            right=Name(id='nFilePerMod', ctx=Load()),
                                        ),
                                        op=Mult(),
                                        right=Name(id='nTemplatePerFile', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='nMod', ctx=Store()),
                                        Name(id='nFilePerMod', ctx=Store()),
                                        Name(id='nTemplatePerFile', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Constant(value=50, kind=None),
                                    Constant(value=5, kind=None),
                                    Constant(value=100, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_sick_script',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='nMod', ctx=Load()),
                                    Name(id='nFilePerMod', ctx=Load()),
                                    Name(id='nTemplatePerFile', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='before', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='now',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                    attr='get_qweb_templates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='addons',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_module_names',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='debug',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='after', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='now',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='delta25000', ctx=Store())],
                            value=BinOp(
                                left=Name(id='after', ctx=Load()),
                                op=Sub(),
                                right=Name(id='before', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='time_ratio', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='delta25000', ctx=Load()),
                                        attr='total_seconds',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Div(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='delta2500', ctx=Load()),
                                        attr='total_seconds',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='runbot',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='Static Templates Inheritance: 25000 templates treated in %s seconds', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='delta25000', ctx=Load()),
                                                attr='total_seconds',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='runbot',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='Static Templates Inheritance: Computed linearity ratio: %s', kind=None),
                                        op=Mod(),
                                        right=Name(id='time_ratio', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertLessEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='time_ratio', ctx=Load()),
                                    Constant(value=12, kind=None),
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
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='-standard', kind=None),
                        Constant(value='static_templates_performance', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
