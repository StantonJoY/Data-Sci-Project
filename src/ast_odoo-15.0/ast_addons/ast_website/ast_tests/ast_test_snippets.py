Module(
    body=[
        ImportFrom(
            module='lxml',
            names=[alias(name='html', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        Import(
            names=[alias(name='odoo.tests', asname=None)],
        ),
        ImportFrom(
            module='odoo.addons.website.tools',
            names=[alias(name='MockRequest', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestSnippets',
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
                    name='test_01_empty_parents_autoremove',
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
                                    Constant(value='/?enable_editor=1', kind=None),
                                    Constant(value='snippet_empty_parent_autoremove', kind=None),
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
                FunctionDef(
                    name='test_02_default_shape_gets_palette_colors',
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
                                    Constant(value='/?enable_editor=1', kind=None),
                                    Constant(value='default_shape_gets_palette_colors', kind=None),
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
                FunctionDef(
                    name='test_03_snippets_all_drag_and_drop',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='MockRequest', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='website',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='website', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='browse',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value=1, kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='snippets_template', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.ui.view', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='render_public_asset',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='website.snippets', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='html_template', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[Name(id='snippets_template', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data_snippet_els', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html_template', ctx=Load()),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="//*[@class='o_panel' and not(contains(@class, 'd-none'))]//*[@data-snippet]", kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='blacklist', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='s_facebook_page', kind=None),
                                    Constant(value='s_map', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='snippets_names', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=',', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Subscript(
                                            value=Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='attrib',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='data-snippet', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='el', ctx=Store()),
                                                iter=Name(id='data_snippet_els', ctx=Load()),
                                                ifs=[
                                                    Compare(
                                                        left=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='el', ctx=Load()),
                                                                attr='attrib',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='data-snippet', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='blacklist', ctx=Load())],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/?enable_editor=1&snippets_names=%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='snippets_names', ctx=Load()),
                                    ),
                                    Constant(value='snippets_all_drag_and_drop', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='admin', kind=None),
                                    ),
                                    keyword(
                                        arg='timeout',
                                        value=Constant(value=300, kind=None),
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
                        Constant(value='website_snippets', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
