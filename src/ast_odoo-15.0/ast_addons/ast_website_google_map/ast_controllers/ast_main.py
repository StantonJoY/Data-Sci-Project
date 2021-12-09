Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.json',
            names=[alias(name='scriptsafe', asname=None)],
            level=0,
        ),
        ClassDef(
            name='GoogleMap',
            bases=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    This class generates on-the-fly partner maps that can be reused in every\n    website page. To do so, just use an ``<iframe ...>`` whose ``src``\n    attribute points to ``/google_map`` (this controller generates a complete\n    HTML5 page).\n\n    URL query parameters:\n    - ``partner_ids``: a comma-separated list of ids (partners to be shown)\n    - ``partner_url``: the base-url to display the partner\n        (eg: if ``partner_url`` is ``/partners/``, when the user will click on\n        a partner on the map, it will be redirected to <myodoo>.com/partners/<id>)\n\n    In order to resize the map, simply resize the ``iframe`` with CSS\n    directives ``width`` and ``height``.\n    ', kind=None),
                ),
                FunctionDef(
                    name='google_map',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='arg', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='clean_ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='partner_id', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='post', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='partner_ids', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=',', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='clean_ids', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[Name(id='partner_id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValueError', ctx=Load()),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partners', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Name(id='clean_ids', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='website_published', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='is_company', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
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
                        Assign(
                            targets=[Name(id='partner_data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='counter', kind=None),
                                    Constant(value='partners', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='partners', ctx=Load())],
                                        keywords=[],
                                    ),
                                    List(elts=[], ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='partner', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='partners', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='show_address',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='partner_data', ctx=Load()),
                                                slice=Constant(value='partners', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='address', kind=None),
                                                    Constant(value='latitude', kind=None),
                                                    Constant(value='longitude', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Constant(value='\n', kind=None),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Subscript(
                                                                            value=Subscript(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='partner', ctx=Load()),
                                                                                        attr='name_get',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[],
                                                                                    keywords=[],
                                                                                ),
                                                                                slice=Constant(value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=1, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='split',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='\n', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                slice=Slice(
                                                                    lower=Constant(value=1, kind=None),
                                                                    upper=None,
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='partner', ctx=Load()),
                                                                attr='partner_latitude',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='partner', ctx=Load()),
                                                                attr='partner_longitude',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
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
                        If(
                            test=Compare(
                                left=Constant(value='customers', kind=None),
                                ops=[In()],
                                comparators=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='post', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='partner_url', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='partner_url', ctx=Store())],
                                    value=Constant(value='/customers/', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='partner_url', ctx=Store())],
                                    value=Constant(value='/partners/', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='google_maps_api_key', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='website',
                                    ctx=Load(),
                                ),
                                attr='google_maps_api_key',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='partner_url', kind=None),
                                    Constant(value='partner_data', kind=None),
                                    Constant(value='google_maps_api_key', kind=None),
                                ],
                                values=[
                                    Name(id='partner_url', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='scriptsafe', ctx=Load()),
                                            attr='dumps',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='partner_data', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='google_maps_api_key', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_google_map.google_map', kind=None),
                                    Name(id='values', ctx=Load()),
                                ],
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
                            args=[
                                List(
                                    elts=[Constant(value='/google_map', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
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
