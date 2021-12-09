Module(
    body=[
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestMailRenderMixin',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_shorten_links',
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
                            targets=[Name(id='test_links', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='<a href="https://gitlab.com" title="title" fake="fake">test_label</a>', kind=None),
                                    Constant(value='<a href="https://test_542152qsdqsd.com"/>', kind=None),
                                    Constant(value='<a href="https://third_test_54212.com">\n                    <img src="imagesrc"/>\n                </a>\n            ', kind=None),
                                    Constant(value='<a\n                    href="https://test_strange_html.com"       title="title"\n                fake=\'fake\'\n                > test_strange_html_label\n                </a>\n            ', kind=None),
                                    Constant(value='<a href="https://test_escaped.com" title="title" fake="fake"> test_escaped &lt; &gt; </a>', kind=None),
                                    Constant(value='<a href="https://url_with_params.com?a=b&c=d">label</a>', kind=None),
                                ],
                                ctx=Load(),
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
                                        slice=Constant(value='mail.render.mixin', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_shorten_links',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='test_links', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='trackers_to_find', ctx=Store())],
                            value=List(
                                elts=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='url', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='https://gitlab.com', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='label', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='test_label', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='url', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='https://test_542152qsdqsd.com', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='url', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='https://test_strange_html.com', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='label', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='test_strange_html_label', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='url', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='https://test_escaped.com', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='label', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='test_escaped < >', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='url', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='https://url_with_params.com?a=b&c=d', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='label', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='label', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='trackers_to_fail', ctx=Store())],
                            value=List(
                                elts=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='url', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='https://test_542152qsdqsd.com', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='label', kind=None),
                                                    Constant(value='ilike', kind=None),
                                                    Constant(value='_', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='tracker_to_find', ctx=Store()),
                            iter=Name(id='trackers_to_find', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='link.tracker', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='tracker_to_find', ctx=Load())],
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
                        For(
                            target=Name(id='tracker_to_fail', ctx=Store()),
                            iter=Name(id='trackers_to_fail', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertFalse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='link.tracker', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='tracker_to_fail', ctx=Load())],
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
