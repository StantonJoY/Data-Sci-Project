Module(
    body=[
        ImportFrom(
            module='odoo.addons.web_editor.controllers.main',
            names=[alias(name='Web_Editor', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.web_unsplash.controllers.main',
            names=[alias(name='Web_Unsplash', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='odoo.tests', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='config', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='BASE_URL', ctx=Store())],
            value=BinOp(
                left=Constant(value='http://127.0.0.1:%s', kind=None),
                op=Mod(),
                right=Tuple(
                    elts=[
                        Subscript(
                            value=Name(id='config', ctx=Load()),
                            slice=Constant(value='http_port', kind=None),
                            ctx=Load(),
                        ),
                    ],
                    ctx=Load(),
                ),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='TestImageUploadProgress',
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
                    name='test_01_image_upload_progress',
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
                                    Constant(value='/test_image_progress', kind=None),
                                    Constant(value='test_image_upload_progress', kind=None),
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
                    name='test_02_image_upload_progress_unsplash',
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
                            name='media_library_search',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='self', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='params', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='results', kind=None),
                                            Constant(value='media', kind=None),
                                        ],
                                        values=[
                                            Constant(value=0, kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='fetch_unsplash_images',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='self', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='post', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='total', kind=None),
                                            Constant(value='total_pages', kind=None),
                                            Constant(value='results', kind=None),
                                        ],
                                        values=[
                                            Constant(value=1434, kind=None),
                                            Constant(value=48, kind=None),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='alt_description', kind=None),
                                                            Constant(value='urls', kind=None),
                                                            Constant(value='links', kind=None),
                                                            Constant(value='user', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='HQqIOc8oYro', kind=None),
                                                            Constant(value='brown fox sitting on green grass field during daytime', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='regular', kind=None)],
                                                                values=[
                                                                    BinOp(
                                                                        left=Name(id='BASE_URL', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Constant(value='/website/static/src/img/phone.png', kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='download_location', kind=None)],
                                                                values=[
                                                                    BinOp(
                                                                        left=Name(id='BASE_URL', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Constant(value='/website/static/src/img/phone.png', kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='links', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Mitchell Admin', kind=None),
                                                                    Dict(
                                                                        keys=[Constant(value='html', kind=None)],
                                                                        values=[Name(id='BASE_URL', ctx=Load())],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                                    value=Name(id='fetch_unsplash_images', ctx=Load()),
                                    attr='routing_type',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='json', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='Web_Unsplash', ctx=Load()),
                                    attr='fetch_unsplash_images',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Call(
                                    func=Attribute(
                                        value=Name(id='http', ctx=Load()),
                                        attr='route',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='/web_unsplash/fetch_images', kind=None)],
                                    keywords=[
                                        keyword(
                                            arg='type',
                                            value=Constant(value='json', kind=None),
                                        ),
                                        keyword(
                                            arg='auth',
                                            value=Constant(value='user', kind=None),
                                        ),
                                    ],
                                ),
                                args=[Name(id='fetch_unsplash_images', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='media_library_search', ctx=Load()),
                                    attr='routing_type',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='json', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='Web_Editor', ctx=Load()),
                                    attr='media_library_search',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Call(
                                    func=Attribute(
                                        value=Name(id='http', ctx=Load()),
                                        attr='route',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[Constant(value='/web_editor/media_library_search', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='type',
                                            value=Constant(value='json', kind=None),
                                        ),
                                        keyword(
                                            arg='auth',
                                            value=Constant(value='user', kind=None),
                                        ),
                                        keyword(
                                            arg='website',
                                            value=Constant(value=True, kind=None),
                                        ),
                                    ],
                                ),
                                args=[Name(id='media_library_search', ctx=Load())],
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
                                    Constant(value='/', kind=None),
                                    Constant(value='test_image_upload_progress_unsplash', kind=None),
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
