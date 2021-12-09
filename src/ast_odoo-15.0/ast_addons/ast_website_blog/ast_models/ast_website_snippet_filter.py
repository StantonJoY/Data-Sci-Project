Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[alias(name='timedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='WebsiteSnippetFilter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='website.snippet.filter', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_hardcoded_sample',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='samples', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_hardcoded_sample',
                                    ctx=Load(),
                                ),
                                args=[Name(id='model', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='model', ctx=Load()),
                                    attr='_name',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='blog.post', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='data', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='cover_properties', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='subtitle', kind=None),
                                                    Constant(value='post_date', kind=None),
                                                    Constant(value='website_url', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='{"background-image": "url(\'/website_blog/static/src/img/cover_2.jpg\')", "resize_class": "o_record_has_cover o_half_screen_height", "opacity": "0"}', kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Islands', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Alone in the ocean', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='fields', ctx=Load()),
                                                                    attr='Date',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='today',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='timedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='days',
                                                                    value=Constant(value=1, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='cover_properties', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='subtitle', kind=None),
                                                    Constant(value='post_date', kind=None),
                                                    Constant(value='website_url', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='{"background-image": "url(\'/website_blog/static/src/img/cover_3.jpg\')", "resize_class": "o_record_has_cover o_half_screen_height", "opacity": "0"}', kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='With a View', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Awesome hotel rooms', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='fields', ctx=Load()),
                                                                    attr='Date',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='today',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='timedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='days',
                                                                    value=Constant(value=2, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='cover_properties', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='subtitle', kind=None),
                                                    Constant(value='post_date', kind=None),
                                                    Constant(value='website_url', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='{"background-image": "url(\'/website_blog/static/src/img/cover_4.jpg\')", "resize_class": "o_record_has_cover o_half_screen_height", "opacity": "0"}', kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Skies', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Taking pictures in the dark', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='fields', ctx=Load()),
                                                                    attr='Date',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='today',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='timedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='days',
                                                                    value=Constant(value=3, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='cover_properties', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='subtitle', kind=None),
                                                    Constant(value='post_date', kind=None),
                                                    Constant(value='website_url', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='{"background-image": "url(\'/website_blog/static/src/img/cover_5.jpg\')", "resize_class": "o_record_has_cover o_half_screen_height", "opacity": "0"}', kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Satellites', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Seeing the world from above', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='fields', ctx=Load()),
                                                                    attr='Date',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='today',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='timedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='days',
                                                                    value=Constant(value=4, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='cover_properties', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='subtitle', kind=None),
                                                    Constant(value='post_date', kind=None),
                                                    Constant(value='website_url', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='{"background-image": "url(\'/website_blog/static/src/img/cover_6.jpg\')", "resize_class": "o_record_has_cover o_half_screen_height", "opacity": "0"}', kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Viewpoints', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Seaside vs mountain side', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='fields', ctx=Load()),
                                                                    attr='Date',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='today',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='timedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='days',
                                                                    value=Constant(value=5, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='cover_properties', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='subtitle', kind=None),
                                                    Constant(value='post_date', kind=None),
                                                    Constant(value='website_url', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='{"background-image": "url(\'/website_blog/static/src/img/cover_7.jpg\')", "resize_class": "o_record_has_cover o_half_screen_height", "opacity": "0"}', kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Jungle', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Spotting the fauna', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='fields', ctx=Load()),
                                                                    attr='Date',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='today',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='timedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='days',
                                                                    value=Constant(value=6, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='merged', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='index', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Call(
                                                func=Name(id='max', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='samples', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='data', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='merged', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            None,
                                                            None,
                                                        ],
                                                        values=[
                                                            Subscript(
                                                                value=Name(id='samples', ctx=Load()),
                                                                slice=BinOp(
                                                                    left=Name(id='index', ctx=Load()),
                                                                    op=Mod(),
                                                                    right=Call(
                                                                        func=Name(id='len', ctx=Load()),
                                                                        args=[Name(id='samples', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='data', ctx=Load()),
                                                                slice=BinOp(
                                                                    left=Name(id='index', ctx=Load()),
                                                                    op=Mod(),
                                                                    right=Call(
                                                                        func=Name(id='len', ctx=Load()),
                                                                        args=[Name(id='data', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='samples', ctx=Store())],
                                    value=Name(id='merged', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='samples', ctx=Load()),
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
