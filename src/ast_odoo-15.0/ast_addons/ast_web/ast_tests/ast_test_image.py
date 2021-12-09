Module(
    body=[
        Import(
            names=[alias(name='io', asname=None)],
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        ImportFrom(
            module='PIL',
            names=[alias(name='Image', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[
                alias(name='HttpCase', asname=None),
                alias(name='tagged', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestImage',
            bases=[Name(id='HttpCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_01_content_image_resize_placeholder',
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
                            value=Constant(value='The goal of this test is to make sure the placeholder image is\n        resized appropriately depending on the given URL parameters.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/web/image/0/200x150', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Image', ctx=Load()),
                                    attr='open',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='io', ctx=Load()),
                                            attr='BytesIO',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='response', ctx=Load()),
                                                attr='content',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='image', ctx=Load()),
                                        attr='size',
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=150, kind=None),
                                            Constant(value=150, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/web/image/fake/0/image_128', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Image', ctx=Load()),
                                    attr='open',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='io', ctx=Load()),
                                            attr='BytesIO',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='response', ctx=Load()),
                                                attr='content',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='image', ctx=Load()),
                                        attr='size',
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=128, kind=None),
                                            Constant(value=128, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/web/image/fake/0/image_256', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Image', ctx=Load()),
                                    attr='open',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='io', ctx=Load()),
                                            attr='BytesIO',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='response', ctx=Load()),
                                                attr='content',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='image', ctx=Load()),
                                        attr='size',
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=256, kind=None),
                                            Constant(value=256, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/web/image/fake/0/image_1024', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Image', ctx=Load()),
                                    attr='open',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='io', ctx=Load()),
                                            attr='BytesIO',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='response', ctx=Load()),
                                                attr='content',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='image', ctx=Load()),
                                        attr='size',
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=256, kind=None),
                                            Constant(value=256, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/web/image/fake/0/image_no_size', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Image', ctx=Load()),
                                    attr='open',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='io', ctx=Load()),
                                            attr='BytesIO',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='response', ctx=Load()),
                                                attr='content',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='image', ctx=Load()),
                                        attr='size',
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=256, kind=None),
                                            Constant(value=256, kind=None),
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
                    name='test_02_content_image_Etag_304',
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
                            value=Constant(value='This test makes sure that the 304 response is properly returned if the ETag is properly set', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='attachment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.attachment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='datas', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='public', kind=None),
                                            Constant(value='mimetype', kind=None),
                                        ],
                                        values=[
                                            Constant(value=b'R0lGODdhAQABAIAAAP///////ywAAAAAAQABAAACAkQBADs=', kind=None),
                                            Constant(value='testEtag.gif', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='image/gif', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/web/image/%s', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='attachment', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='timeout',
                                        value=Constant(value=None, kind=None),
                                    ),
                                ],
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
                                    Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='status_code',
                                        ctx=Load(),
                                    ),
                                    Constant(value=200, kind=None),
                                ],
                                keywords=[],
                            ),
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
                                            value=Name(id='base64', ctx=Load()),
                                            attr='b64encode',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='response', ctx=Load()),
                                                attr='content',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='attachment', ctx=Load()),
                                        attr='datas',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='etag', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='headers',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ETag', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/web/image/%s', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='attachment', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='headers',
                                        value=Dict(
                                            keys=[Constant(value='If-None-Match', kind=None)],
                                            values=[Name(id='etag', ctx=Load())],
                                        ),
                                    ),
                                ],
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
                                    Attribute(
                                        value=Name(id='response2', ctx=Load()),
                                        attr='status_code',
                                        ctx=Load(),
                                    ),
                                    Constant(value=304, kind=None),
                                ],
                                keywords=[],
                            ),
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
                                        args=[
                                            Attribute(
                                                value=Name(id='response2', ctx=Load()),
                                                attr='content',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
