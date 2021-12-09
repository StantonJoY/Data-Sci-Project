Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='pytz', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.http_routing.models.ir_http',
            names=[alias(name='url_for', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules.module',
            names=[alias(name='get_module_resource', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='ustr', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TrackManifest',
            bases=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='webmanifest',
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
                            value=Constant(value=' Returns a WebManifest describing the metadata associated with a web application.\n        Using this metadata, user agents can provide developers with means to create user \n        experiences that are more comparable to that of a native application.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='website', ctx=Store())],
                            value=Attribute(
                                value=Name(id='request', ctx=Load()),
                                attr='website',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='manifest', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='short_name', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='scope', kind=None),
                                    Constant(value='start_url', kind=None),
                                    Constant(value='display', kind=None),
                                    Constant(value='background_color', kind=None),
                                    Constant(value='theme_color', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='website', ctx=Load()),
                                        attr='events_app_name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='website', ctx=Load()),
                                        attr='events_app_name',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[Constant(value='%s Online Events Application', kind=None)],
                                            keywords=[],
                                        ),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='website', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Call(
                                        func=Name(id='url_for', ctx=Load()),
                                        args=[Constant(value='/event', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='url_for', ctx=Load()),
                                        args=[Constant(value='/event', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='standalone', kind=None),
                                    Constant(value='#ffffff', kind=None),
                                    Constant(value='#875A7B', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='icon_sizes', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='192x192', kind=None),
                                    Constant(value='512x512', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='manifest', ctx=Load()),
                                    slice=Constant(value='icons', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=ListComp(
                                elt=Dict(
                                    keys=[
                                        Constant(value='src', kind=None),
                                        Constant(value='sizes', kind=None),
                                        Constant(value='type', kind=None),
                                    ],
                                    values=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='website', ctx=Load()),
                                                attr='image_url',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='website', ctx=Load()),
                                                Constant(value='app_icon', kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='size',
                                                    value=Name(id='size', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        Name(id='size', ctx=Load()),
                                        Constant(value='image/png', kind=None),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='size', ctx=Store()),
                                        iter=Name(id='icon_sizes', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='body', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='dumps',
                                    ctx=Load(),
                                ),
                                args=[Name(id='manifest', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Name(id='ustr', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='make_response',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='body', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='Content-Type', kind=None),
                                                    Constant(value='application/manifest+json', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='response', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/event/manifest.webmanifest', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='GET', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='service_worker',
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
                            value=Constant(value=' Returns a ServiceWorker javascript file scoped for website_event\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='sw_file', ctx=Store())],
                            value=Call(
                                func=Name(id='get_module_resource', ctx=Load()),
                                args=[
                                    Constant(value='website_event_track', kind=None),
                                    Constant(value='static/src/js/service_worker.js', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            Name(id='sw_file', ctx=Load()),
                                            Constant(value='r', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='fp', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='body', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='fp', ctx=Load()),
                                            attr='read',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='js_cdn_url', ctx=Store())],
                            value=Constant(value='undefined', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='website',
                                    ctx=Load(),
                                ),
                                attr='cdn_activated',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='cdn_url', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='website',
                                                            ctx=Load(),
                                                        ),
                                                        attr='cdn_url',
                                                        ctx=Load(),
                                                    ),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='"', kind=None),
                                                    Constant(value='%22', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='\\', kind=None),
                                            Constant(value='%5C', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='js_cdn_url', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='"%s"', kind=None),
                                        op=Mod(),
                                        right=Name(id='cdn_url', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='body', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='body', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='__ODOO_CDN_URL__', kind=None),
                                    Name(id='js_cdn_url', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='make_response',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='body', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='Content-Type', kind=None),
                                                    Constant(value='text/javascript', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='Service-Worker-Allowed', kind=None),
                                                    Call(
                                                        func=Name(id='url_for', ctx=Load()),
                                                        args=[Constant(value='/event', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='response', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/event/service-worker.js', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='GET', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='offline',
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
                            value=Constant(value=" Returns the offline page used by the 'website_event' PWA\n        ", kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='website_event_track.pwa_offline', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/event/offline', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='GET', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
