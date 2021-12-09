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
            module='odoo.tools.translate',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ClassDef(
            name='WebsiteBackend',
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
                    name='fetch_dashboard_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='website_id', annotation=None, type_comment=None),
                            arg(arg='date_from', annotation=None, type_comment=None),
                            arg(arg='date_to', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='Website', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='website', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='has_group_system', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='has_group',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.group_system', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='has_group_designer', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='has_group',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='website.group_website_designer', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dashboard_data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='groups', kind=None),
                                    Constant(value='currency', kind=None),
                                    Constant(value='dashboards', kind=None),
                                ],
                                values=[
                                    Dict(
                                        keys=[
                                            Constant(value='system', kind=None),
                                            Constant(value='website_designer', kind=None),
                                        ],
                                        values=[
                                            Name(id='has_group_system', ctx=Load()),
                                            Name(id='has_group_designer', ctx=Load()),
                                        ],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='visits', kind=None)],
                                        values=[Dict(keys=[], values=[])],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='current_website', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='website_id', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='Website', ctx=Load()),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='website_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='Website', ctx=Load()),
                                            attr='get_current_website',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='multi_website', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='has_group',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='website.group_multi_website', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='websites', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='multi_website', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='website', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[List(elts=[], ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Name(id='current_website', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='dashboard_data', ctx=Load()),
                                    slice=Constant(value='websites', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='websites', ctx=Load()),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='rec', ctx=Store()),
                                    Name(id='website', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='zip', ctx=Load()),
                                args=[
                                    Name(id='websites', ctx=Load()),
                                    Subscript(
                                        value=Name(id='dashboard_data', ctx=Load()),
                                        slice=Constant(value='websites', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='website', ctx=Load()),
                                            slice=Constant(value='domain', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='_get_http_domain',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='website', ctx=Load()),
                                            slice=Constant(value='id', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='current_website', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='website', ctx=Load()),
                                                    slice=Constant(value='selected', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='has_group_designer', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='current_website', ctx=Load()),
                                                attr='google_management_client_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='current_website', ctx=Load()),
                                                attr='google_analytics_key',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='dashboard_data', ctx=Load()),
                                                        slice=Constant(value='dashboards', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='visits', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='ga_client_id',
                                                        value=BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='current_website', ctx=Load()),
                                                                    attr='google_management_client_id',
                                                                    ctx=Load(),
                                                                ),
                                                                Constant(value='', kind=None),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='ga_analytics_key',
                                                        value=BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='current_website', ctx=Load()),
                                                                    attr='google_analytics_key',
                                                                    ctx=Load(),
                                                                ),
                                                                Constant(value='', kind=None),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='dashboard_data', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/website/fetch_dashboard_data', kind=None)],
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
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='website_set_ga_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='website_id', annotation=None, type_comment=None),
                            arg(arg='ga_client_id', annotation=None, type_comment=None),
                            arg(arg='ga_analytics_key', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='has_group',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.group_system', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='title', kind=None),
                                                    Constant(value='message', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Access Error', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='You do not have sufficient rights to perform that action.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='ga_analytics_key', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='ga_client_id', ctx=Load()),
                                                attr='endswith',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='.apps.googleusercontent.com', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='title', kind=None),
                                                    Constant(value='message', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Incorrect Client ID / Key', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='The Google Analytics Client ID or Key you entered seems incorrect.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='Website', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='website', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='current_website', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='website_id', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='Website', ctx=Load()),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='website_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='Website', ctx=Load()),
                                            attr='get_current_website',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
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
                                                slice=Constant(value='res.config.settings', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='google_management_client_id', kind=None),
                                                    Constant(value='google_analytics_key', kind=None),
                                                    Constant(value='website_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='ga_client_id', ctx=Load()),
                                                    Name(id='ga_analytics_key', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='current_website', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/website/dashboard/set_ga_data', kind=None)],
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
